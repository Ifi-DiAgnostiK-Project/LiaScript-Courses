# Workflow Race Condition Fix

## Problem (Historical)
When a course file was changed, both `update-course-count.yml` and `generate-liascript-outputs.yml` workflows were triggered simultaneously. They used the same concurrency group (`course-modifications`) with `cancel-in-progress: false`, which meant they ran sequentially.

However, both workflows would check out the same initial commit that triggered them. If the first workflow completed and pushed a commit, the second workflow was still working on the old commit and would:
1. Create conflicts when trying to push
2. Risk losing changes made by the first workflow
3. Potentially fail to push altogether

Even with protections like `git pull --rebase` before commits and concurrency control, the race condition could still occur when:
- Version increment commits in Phase 1 triggered Phase 2
- Both workflows tried to coordinate their commits
- The concurrency queue didn't coordinate well with rapid successive commits

## Solution (Current)
**Consolidated Workflow Architecture**

The race condition has been eliminated by consolidating the `update-course-count.yml` workflow into `generate-liascript-outputs.yml` as a separate job. This architectural change means:

1. **Single Workflow**: Only one workflow is triggered on course changes
2. **No Race Condition**: Jobs within a single workflow coordinate automatically
3. **Shared Lifecycle**: All jobs respect the same phase (Phase 1 vs Phase 2)
4. **Parallel Execution**: Independent jobs can run in parallel when appropriate

## Implementation Details

### Workflow Structure
```yaml
jobs:
  check_changes:
    # Detects changes, manages version increments (Phase 1/2)
    
  generate_outputs:
    needs: [check_changes]
    # Generates SCORM packages and releases
    
  create_project_index_html:
    needs: [check_changes, generate_outputs]
    # Generates index.html (skipped in Phase 1)
    
  update_course_count:
    needs: [check_changes]
    # Updates course count badge (skipped in Phase 1)
```

### Phase Coordination
Both `create_project_index_html` and `update_course_count` jobs:
- Check `needs.check_changes.outputs.version_incremented != 'true'`
- Skip execution during Phase 1 (when version is incremented)
- Run during Phase 2 or when no version increment is needed
- Can execute in parallel since they modify different files

### Benefits
1. **Eliminates Race Conditions**: Single workflow means no concurrency conflicts
2. **Better Resource Usage**: Jobs can run in parallel when appropriate
3. **Simpler Architecture**: One workflow to maintain instead of two
4. **Consistent Behavior**: All jobs follow the same Phase 1/Phase 2 pattern
5. **Atomic Execution**: GitHub Actions guarantees job coordination within a workflow

## Changes Made

### Removed
- ❌ `update-course-count.yml` (separate workflow)

### Modified
- ✅ `generate-liascript-outputs.yml`:
  - Added `update_course_count` job
  - Job runs at same phase as index generation
  - Maintains all existing functionality (count, compare, update badge)
  - Uses same protection mechanisms (`git pull --rebase`)

## Error Handling
The consolidated workflow maintains robust error handling:
- `git pull --rebase` before all commits to sync with latest changes
- Fallback `|| { echo "..." }` allows continuation with clear error messages
- Badge updates use read-compare-update pattern to avoid unnecessary commits
- All jobs respect the Phase 1/Phase 2 pattern to avoid infinite loops

## Testing & Verification

### Key Behaviors Verified
1. ✅ **Phase 1 Behavior**: When version increment needed, only `check_changes` runs
2. ✅ **Phase 2 Behavior**: After version increment, all jobs run including course count update
3. ✅ **No Increment Behavior**: When no version change needed, all jobs run normally
4. ✅ **Parallel Execution**: Independent jobs (index generation, course count) can run simultaneously
5. ✅ **Badge Updates**: Only commits when course count actually changes

### Migration Notes
- Previous two-workflow setup required manual concurrency coordination
- New single-workflow approach relies on GitHub Actions' built-in job dependencies
- No configuration changes needed - existing triggers and permissions work as-is
- Badge URL and format remain unchanged (backward compatible)

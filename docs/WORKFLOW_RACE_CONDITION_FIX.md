# Workflow Race Condition Fix

## Problem
When a course file is changed, both `update-course-count.yml` and `generate-liascript-outputs.yml` workflows are triggered simultaneously. They use the same concurrency group (`course-modifications`) with `cancel-in-progress: false`, which means they run sequentially.

However, both workflows check out the same initial commit that triggered them. If the first workflow completes and pushes a commit, the second workflow is still working on the old commit and may:
1. Create conflicts when trying to push
2. Lose the changes made by the first workflow
3. Fail to push altogether

## Solution
Before each commit in both workflows, we now run:
```bash
git pull --rebase origin main || {
  echo "Failed to pull latest changes, attempting to continue anyway"
}
```

This ensures that:
1. Each workflow pulls the latest changes before committing
2. Local changes are rebased on top of any new commits
3. No commits are lost
4. Push conflicts are minimized

## Changes Made
Added `git pull --rebase` before commits in:
- `update-course-count.yml`: Before badge data commit (line ~114)
- `generate-liascript-outputs.yml`: 
  - Before version increment commit (line ~106)
  - Before checksum state commit (line ~148)
  - Before index.html commit (line ~334)

## Error Handling
The `|| { echo "..." }` fallback allows the workflow to continue even if the pull fails. This is intentional:
- If there's a genuine conflict, the push will fail with a clear error
- Users can re-run the workflow after resolving the issue
- This is better than silently failing or losing commits

## Testing
The fix has been tested against multiple scenarios:
1. ✅ update-course-count runs first
2. ✅ generate-liascript-outputs runs first  
3. ✅ Multiple commits during workflow execution
4. ✅ Edge cases with rebase conflicts

All scenarios now handle race conditions correctly without losing commits.

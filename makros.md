<!--
author: Volker Göhler
email:    volker.goehler@informatik.tu-freiberg.de
language: de
narrator: German Female
version: 0.0.1
comment: this makro package defines styles and a header with badges for the LiaScript course, we also include our image repository

@style
.flex-container {
    display: flex;
    flex-wrap: wrap; /* Allows the items to wrap as needed */
    align-items: stretch;
    gap: 20px; /* Adds both horizontal and vertical spacing between items */
}

.flex-child { 
    flex: 1;
    margin-right: 20px; /* Adds space between the columns */
}

@media (max-width: 600px) {
    .flex-child {
        flex: 100%; /* Makes the child divs take up the full width on slim devices */
        margin-right: 0; /* Removes the right margin */
    }
}
@end

import: https://raw.githubusercontent.com/vgoehler/DiAgnostiK_Bilder_Test/refs/heads/main/makros.md

-->

# Do we crash without a header?     


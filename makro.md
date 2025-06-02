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

@include: https://raw.githubusercontent.com/vgoehler/DiAgnostiK_Bilder_Test/refs/heads/main/makros.md

@header

# LiaScript Badges

[![LiaScript Course](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?
@0?raw=true
)

[![LiaScript LiveEditor](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/LiveEditor/?/show/file/
@0?raw=true
)

[![GitHub](https://img.shields.io/badge/Ansehen%20auf-GitHub-181717?logo=github)](
@0
)

[![Rohinhalt](https://img.shields.io/badge/Raw-Inhalt-blue)](
@0?raw=true
)

@end

-->


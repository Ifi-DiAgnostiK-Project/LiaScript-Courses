<!--
author: Volker Göhler
email: volker.goehler@informatik.tu-freiberg.de
version: 0.0.12
edit: true
date: 2025-05-20
logo: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
comment: Test Course for the action release system

title : Test Course for Action Release System

tags:
    - Experimente

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Holzarten/refs/heads/main/makros.md

@style
.flex-container {
    display: flex;[](https://liascript.github.io/LiveEditor/liascript/index.html?#5)
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

-->
 
# Test Course in LiaScript

> s.u. ohne die srcs, definition im holzarten Kurs, mich wundert das das funktioniert, weil die imgs in divs verpackt sind.
> Richtige Beantwortung funktioniert scheinbar nicht 😏

@dragdropmultiple(@uid, @Hoelzer1.Robinie | @Hoelzer2.Laerche, @Hoelzer1.Ahorn )

> @Hoelzer1.Pockholz.src
> Das wird unten gar nicht dargestellt -> gibt es hier ein Problem mit dem "compile" vom Live Editor?

@dragdropmultiple(@uid, @Hoelzer1.Robinie.src | @Hoelzer2.Laerche.src , @Hoelzer1.Ahorn.src, @Hoelzer1.Pockholz.src, @Hoelzer1.Elsbeere.src )


- all courses in courses will be release handled if there are changes detected
- action will be triggered with every commit that changes a markdown in courses
- ~need to set the github pages still~ -> pages is setup: ~[pages link](https://vgoehler.github.io/DiAgnostiK_LiaScript/)~ [new page]{https://ifi-diagnostik-project.github.io/LiaScript-Courses/}

# liascript example

| Zeichen | Typ|
|--- | ---|
|@Rettungszeichen.Erste_Hilfe(10) | Rettungszeichen|
|@Warnzeichen.Automatischer_Anlauf(10) | Warnzeichen|
|@Gefahrstoffe.Komprimierte_Gase(10) | Gefahrstoff|

function nav_button() {
    let main = document.querySelector("main");
    let footer = document.querySelector("footer");
    let button = document.querySelector(".nav-button");
    let navigation = document.querySelector(".navigation");


    main.classList.toggle("shifted");
    footer.classList.toggle("shifted");
    button.classList.toggle("rotated");
    navigation.classList.toggle("shifted");
}


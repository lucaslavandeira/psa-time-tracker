

window.addEventListener("load", (e) => {
   hovers();
});


function hovers() {
    const docs = document.getElementsByClassName("project");
    for (let i = 0; i < docs.length; i++) {
        let d = docs.item(i);
        d.addEventListener("mouseover", (e) => {
            d.classList.add("active");
        });

        d.addEventListener("mouseleave", (e) => {
            d.classList.remove("active");
        });

    }
}
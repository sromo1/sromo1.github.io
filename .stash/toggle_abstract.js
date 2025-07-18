function toggleAbstract(element) {
    var abstract = element.nextElementSibling;

    if (abstract.style.display === "none") {
        abstract.style.display = "block";
        element.querySelector('.arrow').classList.add('rotated');
        element.innerHTML = element.innerHTML.replace('Show', 'Hide');
    } else {
        abstract.style.display = "none";
        element.querySelector('.arrow').classList.remove('rotated');
        element.innerHTML = element.innerHTML.replace('Hide', 'Show');
    }
}
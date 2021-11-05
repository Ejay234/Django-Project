const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.links');

menu.addEventListener('click', function () {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
});

//function togglePopup() {
//    document.getElementById("popup-1").classList.toggle("active");
//};
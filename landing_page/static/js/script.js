const selector = selector => document.querySelector(selector);
const selectorAll = selector => document.querySelectorAll(selector);

const hamburguer = selector('.menu-hamburguer');
const hamburguerNav = selector('.nav-menu-hamburguer');

hamburguer.onclick = function () {
    hamburguer.classList.toggle('ativo');
    hamburguerNav.classList.toggle('visible');
}


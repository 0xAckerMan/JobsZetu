var swiper = new Swiper(".mySwiper", {
    effect: "flip",
    // grabCursor: true,
    loop: true,
    speed: 1500,
    pagination: {
        el: ".swiper-pagination",
    },
    navigation: {
        nextEl: ".Signup",
        prevEl: ".Signup",
    },
    
});

// home swiper
var swiper2 = new Swiper(".mySwiperhome", {
    effect: "fade",
    // grabCursor: true,
    spaceBetween: 30,
    loop: true,
    speed: 1500,
    pagination: {
        el: ".swiper-pagination",
        clickabe: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    autoplay: {
        delay: 5500,
        disableOnInteraction: true,
    },
    
});


// home page swiper
var swiper3 = new Swiper(".mySwiperhome", {
    effect: "fade",
    // grabCursor: true,
    spaceBetween: 30,
    loop: true,
    speed: 1500,
    pagination: {
        el: ".swiper-pagination",
        clickabe: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    autoplay: {
        delay: 5500,
        disableOnInteraction: true,
    },
    
});



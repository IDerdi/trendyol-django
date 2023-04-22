var swiper1 = new Swiper('.swiper1', {
    slidesPerView: 11,
    spaceBetween: 20,
    slidesPerGroup: 11,
    breakpoints: {
        // when window width is >= 320px
        320: {
            slidesPerView: 4,
            spaceBetween: 20,
            slidesPerGroup: 4,
        },
        // when window width is >= 480px
        700: {
            slidesPerView: 6,
            spaceBetween: 20,
            slidesPerGroup: 6,
          
        },
        // when window width is >= 640px
        1000: {
            slidesPerView: 11,
            spaceBetween: 20,
            slidesPerGroup: 11,
        }},

        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
   
  });
  
  var swiper2 = new Swiper('.swiper2', {
    slidesPerView: 5,
    spaceBetween: 20,
    slidesPerGroup: 5,
    breakpoints: {
      // when window width is >= 320px
      200: {
          slidesPerView: 2,
          spaceBetween: 20,
          slidesPerGroup: 2,
      },
      // when window width is >= 480px
      760: {
          slidesPerView: 3,
          spaceBetween: 20,
          slidesPerGroup: 3,
        
      },
      // when window width is >= 640px
      1400: {
          slidesPerView: 5,
          spaceBetween: 20,
          slidesPerGroup: 5,
      }},

        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
   
  });
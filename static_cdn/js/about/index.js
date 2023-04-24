$(document).ready(function() {
    "use strict";
    
    new WOW().init();

    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });

})

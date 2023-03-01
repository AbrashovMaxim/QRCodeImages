$('.img_base, .img_qr').on('click', (e) => {
    const getSrc = $(e.target).attr('src');
    $('body').append("<div class='modal'>"+
                        "<img src='" + getSrc + "'>"+
                    "</div>");
});

$('body').on('click', '.modal', (e) => { $('.modal').remove(); });
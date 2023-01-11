(function ($) {
   $('.update-cart').on('click', async function () {
        let action = $(this).data('action');
        let productId = $(this).data('product');

        await fetch('/update_item/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({'productId': productId, 'action': action})
        })


    })
})(jQuery)
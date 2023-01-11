(function ($) {
    $('.update-cart').on('click', async function () {
        let item = $(this).closest('tr');
        let action = $(this).data('action');
        let productId = item.data('product');
        let price = item.data('price');

        await fetch('/update_item/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({'productId': productId, 'action': action})
        })
        console.log(productId)

        let quantity = item.find(`.item-quantity`).val();
        let totalPrice = item.find('.item-total-price');

        if (quantity <= 0) {
            item.remove();
            return;
        } else if (action === 'delete') {
            item.remove();
            return;
        }

        totalPrice.text(`$${quantity * price}`);
    })

})(jQuery)



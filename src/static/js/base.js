(async function($) {
    let response = await fetch("/order_items/");
    let data = await response.json();

    console.log(data)
})(jQuery)
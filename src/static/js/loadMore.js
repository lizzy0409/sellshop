// $(document).ready(function () {
//     $("#loadMore").on('click', function () {
//         let currentProducts = $(".product-box").length;
//         let limit = $(this).attr("data-limit");
//         let total = $(this).attr("data-total");
//
//         $.ajax({
//             url: '/load-more-data',
//             data: {
//                 limit: limit,
//                 offset: currentProducts
//             },
//             dataType: 'json',
//             beforeSend: function () {
//                 $("#loadMore").attr('disabled', true);
//             },
//             success: function (res) {
//                 $("#featured-products").append(res.data);
//                 $("#loadMore").attr('disabled', false);
//
//                 let totalShowing = $(".product-box").length;
//                 if (totalShowing === total) {
//                     $("#loadMore").remove();
//                 }
//             }
//         });
//     });
// });
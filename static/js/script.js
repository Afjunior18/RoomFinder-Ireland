// Function to show the awaiting approval confirmation modal
function showMessageModal(message) {
    $('#messageBody').html(message);
    $('#messageModal').modal('show');
}

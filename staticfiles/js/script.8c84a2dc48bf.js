function showMessageModal(message) {
    $('#messageBody').html(message);
    $('#messageModal').modal('show');
}

showMessageModal('Room submitted and awaiting approval');
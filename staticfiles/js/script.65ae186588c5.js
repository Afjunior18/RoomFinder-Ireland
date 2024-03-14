function showMessageModal(message) {
    jQuery('#messageBody').html(message);
    jQuery('#messageModal').modal('show');
}

showMessageModal('Room submitted and awaiting approval');
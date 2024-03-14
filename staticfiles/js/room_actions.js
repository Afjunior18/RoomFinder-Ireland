$(document).ready(function() {
    // modal to delete a room post
    $('#custom-btn-delete').click(function() {
        console.log('Botão de exclusão clicado');
        $('#deleteRoomModal').modal('show');
    });

    // modal to approve a room post
    $('#custom-btn-approve').click(function() {
        console.log('Botão de aprovação clicado');
        $('#approveRoomModal').modal('show');
    });
});
$(document).ready(function() {
    // Abrir modal de confirmação de exclusão
    $('#custom-btn-delete').click(function() {
        console.log('Botão de exclusão clicado');
        $('#deleteRoomModal').modal('show');
    });

    // Abrir modal de confirmação de aprovação
    $('#custom-btn-approve').click(function() {
        console.log('Botão de aprovação clicado');
        $('#approveRoomModal').modal('show');
    });
});
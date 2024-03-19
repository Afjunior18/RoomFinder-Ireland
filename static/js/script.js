// Function to show the awaiting approval confirmation modal
function showMessageModal(message) {
    $('#messageBody').html(message);
    $('#messageModal').modal('show');
}

// Button Delete and Confirmation Modal

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Button Edit

const editButtons = document.querySelectorAll(".btn-edit");


// Add event listener to delete button

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let roomId = e.target.getAttribute("data-room-id");
        deleteConfirm.href = `/delete/${roomId}/`;
        deleteModal.show();
    });
}

// Add event listener to Edit button

editButtons.forEach(button => {
    button.addEventListener('click', () => {
        const roomId = button.getAttribute('data-room-id');
        window.location.href = `/edit/${roomId}/`;
    });
});
// Function to show the awaiting approval confirmation modal
function showMessageModal(message) {
    $('#messageBody').html(message);
    $('#messageModal').modal('show');
}

// Button Delete and Confirmation Modal

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Add event listener to delete button

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let roomId = e.target.getAttribute("data-room-id");
        deleteConfirm.href = `/room_finder/delete_room/${roomId}/`;
        deleteModal.show();
    });
}

// Add event listener to delete confirmation button

deleteConfirm.addEventListener("click", (e) => {
    e.preventDefault(); // Prevent the default action (opening the href)
    window.location.href = deleteConfirm.href; // Navigate to the delete URL
});
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
        deleteConfirm.href = `/delete/${roomId}/`;
        deleteModal.show();
    });
}




const nextPhotoButton = document.querySelector(".carousel-control-next");
const previousPhotoButton = document.querySelector(".carousel-control-prev");
const carousel = document.querySelector("#carouselExampleCaptions");

nextPhotoButton.addEventListener("click", function() {
    carousel.querySelector(".carousel-item.active").nextElementSibling.click();
});

previousPhotoButton.addEventListener("click", function() {
    carousel.querySelector(".carousel-item.active").previousElementSibling.click();
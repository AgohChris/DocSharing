document.addEventListener('DOMContentLoaded', function() {
    const profilePictureInput = document.getElementById('id_profile_picture');
    const profilePicturePreview = document.getElementById('profile-picture-preview');

    profilePictureInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                profilePicturePreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
});
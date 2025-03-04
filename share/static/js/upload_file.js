document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('id_file');
    const filePreview = document.querySelector('.file-preview');

    fileInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.createElement('img');
                img.src = e.target.result;
                filePreview.innerHTML = '';
                filePreview.appendChild(img);
            };
            reader.readAsDataURL(file);
        }
    });
});


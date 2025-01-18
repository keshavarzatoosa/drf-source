// static/js/admin_parameters.js
document.addEventListener('DOMContentLoaded', function() {
    const parentField = document.getElementById('id_parent');
    const typeField = document.getElementById('id_type');

    if (parentField && typeField) {
        parentField.addEventListener('change', function() {
            const parentId = this.value;
            if (parentId) {
                fetch(`/admin/parameters/parameters/${parentId}/change/`)
                    .then(response => response.text())
                    .then(html => {
                        const parser = new DOMParser();
                        const doc = parser.parseFromString(html, 'text/html');
                        const parentType = doc.getElementById('id_type').value;
                        typeField.value = parentType;
                        typeField.readOnly = true;
                    });
            } else {
                typeField.value = '';
                typeField.readOnly = false;
            }
        });
    }
});
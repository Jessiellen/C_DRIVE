export default class DriveModel {
    #folders = [];

    constructor() {
        if (!localStorage.getItem("c_drive")) {
            localStorage.setItem("c_drive", JSON.stringify(this.#folders));
        } else {
            this.#folders = JSON.parse(localStorage.getItem("c_drive"));
        }
    }

    /** FOLDERS */
    addFolder(folder) {
        this.#folders.push({ title: folder, items: [] });
        this.#updateLocalStorage();
    }

    deleteFolder(index) {
        this.#folders.splice(index, 1);
        this.#updateLocalStorage();
    }

    getFolders() {
        return this.#folders;
    }

    /** FILES */
    addFile(folderIndex, file) {
        this.#folders[folderIndex].items.push({ title: file, checked: false });
        this.#updateLocalStorage();
    }

    deleteFile(folderIndex, fileIndex) {
        this.#folders[folderIndex].items.splice(fileIndex, 1);
        this.#updateLocalStorage();
    }

    updateFile(folderIndex, fileIndex, val) {
        this.#folders[folderIndex].items[fileIndex].checked = val;
        this.#updateLocalStorage();
    }

    getFiles(folderIndex) {
        return this.#folders[folderIndex].items;
    }

    #updateLocalStorage() {
        localStorage.setItem("c_drive", JSON.stringify(this.#folders));
    }
}


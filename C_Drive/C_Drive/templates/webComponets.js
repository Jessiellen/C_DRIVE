const headerTemplate = document.createElement("template");
headerTemplate.innerHTML = `
<style>
    @import url("styles.css");
    :host {
        display: block;
        background-color: #EEEEEE;
        color: 5F81D9;
        padding: 16px;
    }
    h1 {
        margin: 0;
    }
</style>
<header>
    <h1>C_Drive</h1>
</header>
`;

class C_DriveHeader extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' }).append(headerTemplate.content.cloneNode(true));
    }
}

customElements.define('c_drive-header', 
C_DriveHeader);

const fileItemTemplate = document.createElement("template");
fileItemTemplate.innerHTML = `
<style>
    @import url("styles.css");
    :host {
        display: block;
        padding: 16px;
        border-bottom: 1px solid;
        cursor: pointer;
    }
    .file-item {
        display: flex;
        align-items: center;
    }
    .file-icon {
        margin-right: 8px;
    }
</style>
<div class="file-item">
    <span class="file-icon"></span>
    <span class="file-name"></span>
</div>
`;

class FileItem extends HTMLElement {
    static get observedAttributes() {
        return ['file-name'];
    }

    constructor() {
        super();
        this.attachShadow({ mode: 'open' }).append(fileItemTemplate.content.cloneNode(true));
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (name === 'file-name') {
            this.shadowRoot.querySelector('.file-name').textContent = newValue;
        }
    }
}

customElements.define('file-item', FileItem);

// Editor.js
import React from 'react';
import { Editor } from '@tinymce/tinymce-react';
import './Editor.css';
import { useRef } from 'react';

const EditorComponent = ({ content, onContentChange }) => {

    const editorRef = useRef(null);

    return (
        <>
            <Editor
                tinymceScriptSrc='/tinymce/tinymce.min.js'
                onInit={(_evt, editor) => editorRef.current = editor}
                init={{
                    license_key: 'gpl',
                    branding: false,
                    menubar: false,
                    height: 500,
                    visual: false,
                    html: false,
                    selector: 'textarea',
                    plugins: [
                        'advlist', 'autolink', 'lists', 'link', 'image', 'charmap',
                        'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
                        'insertdatetime', 'media', 'table', 'preview', 'help', 'wordcount'
                    ],
                    toolbar: 'undo redo | blocks | ' +
                        'bold italic forecolor | alignleft aligncenter ' +
                        'alignright alignjustify | bullist numlist outdent indent | ' +
                        'removeformat | help',
                    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
                }}
            />
        </>
    );
}

export default EditorComponent;

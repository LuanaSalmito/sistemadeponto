import React, { useState } from 'react';
import { Container, Button, Form, Row, Col } from 'react-bootstrap';
import EditorComponent from '../editor/Editor'; // Editor existente

const ReescritaPostagemForm = () => {
  const [textoOriginal, setTextoOriginal] = useState('');
  const [plataforma, setPlataforma] = useState('');
  const [tom, setTom] = useState('');
  const [editorContent, setEditorContent] = useState('');
  const [outputContent, setOutputContent] = useState('');

  const handleEditorChange = (content) => {
    setEditorContent(content);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Simulação de lógica para processar os dados e reescrever o texto
    setOutputContent(`
      Plataforma: ${plataforma}
      Tom: ${tom}
      Texto Original: ${textoOriginal}
      Reescrita Gerada: (Aqui seria a resposta gerada pela IA com base nos parâmetros fornecidos)
    `);
  };

  return (
<div>
      <h1 className="mb-4">Reescrita de Postagem com IA</h1>
      <Row>
        {/* Formulário à esquerda */}
        <Col md={4}>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="textoOriginal" className="mb-3">
              <Form.Label>Texto Original</Form.Label>
              <Form.Control
                as="textarea"
                rows={5}
                placeholder="Insira o texto que deseja reescrever"
                value={textoOriginal}
                onChange={(e) => setTextoOriginal(e.target.value)}
                required
              />
            </Form.Group>

            <Form.Group controlId="plataforma" className="mb-3">
              <Form.Label>Plataforma Destinada</Form.Label>
              <Form.Select
                value={plataforma}
                onChange={(e) => setPlataforma(e.target.value)}
                required
              >
                <option value="">Selecione uma plataforma</option>
                <option value="Instagram">Instagram</option>
                <option value="LinkedIn">LinkedIn</option>
                <option value="Twitter">Twitter</option>
                <option value="Facebook">Facebook</option>
              </Form.Select>
            </Form.Group>

            <Form.Group controlId="tom" className="mb-3">
              <Form.Label>Tom da Reescrita</Form.Label>
              <Form.Select
                value={tom}
                onChange={(e) => setTom(e.target.value)}
                required
              >
                <option value="">Selecione um tom</option>
                <option value="Formal">Formal</option>
                <option value="Casual">Casual</option>
                <option value="Inspirador">Inspirador</option>
                <option value="Informativo">Informativo</option>
              </Form.Select>
            </Form.Group>

            <Button type="submit" className="w-100">
              Gerar Reescrita
            </Button>
          </Form>
        </Col>

        {/* Editor e Resultado à direita */}
        <Col md={8}>
          <Form.Group controlId="editor" className="mb-3">
            <Form.Label>Editor de Texto</Form.Label>
            <EditorComponent content={editorContent} onContentChange={handleEditorChange} />
          </Form.Group>

          {outputContent && (
            <div className="mt-4">
              <h4>Resultado Gerado:</h4>
              <pre className="border p-3">{outputContent}</pre>
            </div>
          )}
        </Col>
      </Row></div>
  );
};

export default ReescritaPostagemForm;

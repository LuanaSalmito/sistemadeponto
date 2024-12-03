import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom'; // Importar useNavigate
import { Container, Row, Col, Form, InputGroup, Button, Spinner, Alert } from 'react-bootstrap';
import QRCode from 'react-qr-code';
import plans from './plansData';

function Checkout() {
  const { planId } = useParams();
  const navigate = useNavigate(); // Inicializar useNavigate
  const plan = plans.find((p) => p.id === planId);
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [step, setStep] = useState(1);
  const [termsAccepted, setTermsAccepted] = useState(false);
  const [pixCode, setPixCode] = useState('');
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  const MAIN_URL = process.env.REACT_APP_MAIN;

  if (!plan) {
    return (
      <Container className="my-5">
        <h2>Plano não encontrado</h2>
        <p>O plano selecionado não existe.</p>
      </Container>
    );
  }

  // Simulação de requisição para o backend
  const fetchPixCode = () => {
    setLoading(true);
    setTimeout(() => {
      // Código Pix falso retornado pelo "backend"
      const fakePixCode =
        '00020126580014BR.GOV.BCB.PIX0136d2b64a74-12d2-4fcb-a9d3-1234567890520brlvalor101234.56170512PedidoXPTO53039865802BR5925Fulano+de+Tal6008Brasília62240525';
      setPixCode(fakePixCode);
      setLoading(false);
    }, 2000);
  };

  const handleNextStep = () => {
    if (step === 1) {
      if (!email || !phone) {
        alert('Por favor, preencha todos os campos!');
        return;
      }
      if (!termsAccepted) {
        alert('Você precisa aceitar os Termos de Serviço para continuar.');
        return;
      }
      setStep(2);
      fetchPixCode(); // Simula a requisição ao backend ao avançar
    }
  };

  const handlePreviousStep = () => {
    if (step === 2) {
      setStep(1);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(pixCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000); // Feedback desaparece após 2 segundos
  };

  const goToLandingPage = () => {
    navigate(`${MAIN_URL}`); // Redireciona para a landing page
  };  

  const goToDashboard = () => {
    navigate(`${MAIN_URL}dashboard`); // Redireciona para o dashboard
  };

  return (
    <Container className="my-5">
      
        
          <Button variant="outline-secondary mb-3" onClick={goToLandingPage}>
            Voltar para a página inicial
          </Button>
      <Row>
        {/* Coluna da descrição do plano */}
        <Col md={6} className="bg-dark text-white p-4">
          <h2 className="mb-4">{plan.name}</h2>
          <h3 className="display-4 mb-3">{plan.price}</h3>
          <p className="mb-4">Plano ipsum: lorem ipsum damet et al</p>
          <ul className="list-unstyled">
            {plan.perks.map((perk, index) => (
              <li key={index} className="mb-2">
                <i className="bi bi-check-circle-fill text-primary me-2"></i>
                {perk}
              </li>
            ))}
          </ul>
          <hr className="border-light" />
          <div className="d-flex justify-content-between align-items-center mt-4">
            <span>Subtotal:</span>
            <span>{plan.price}</span>
          </div>
          <div className="d-flex justify-content-between align-items-center mb-4">
            <span>Total devido hoje:</span>
            <span>{plan.price}</span>
          </div>
        </Col>

        {/* Coluna dinâmica */}
        <Col md={6} className="bg-light p-4">
          {step === 1 ? (
            <>
              <Form className="mb-4">
                <Form.Group controlId="email" className="mb-3">
                  <Form.Label>Email</Form.Label>
                  <InputGroup>
                    <InputGroup.Text>@</InputGroup.Text>
                    <Form.Control
                      type="email"
                      placeholder="Digite seu email"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                    />
                  </InputGroup>
                </Form.Group>
                <Form.Group controlId="phone" className="mb-3">
                  <Form.Label>Telefone</Form.Label>
                  <InputGroup>
                    <InputGroup.Text>📞</InputGroup.Text>
                    <Form.Control
                      type="tel"
                      placeholder="(XX) XXXXX-XXXX"
                      value={phone}
                      onChange={(e) => setPhone(e.target.value)}
                    />
                  </InputGroup>
                </Form.Group>
                <Form.Group controlId="terms" className="mt-4">
                  <Form.Check
                    type="checkbox"
                    label="Concordo com os Termos de Serviço e a Política de Privacidade"
                    checked={termsAccepted}
                    onChange={(e) => setTermsAccepted(e.target.checked)}
                  />
                </Form.Group>
              </Form>
              <div className="text-center mt-3">
                <Button variant="primary" size="lg" onClick={handleNextStep}>
                  Confirmar
                </Button>
              </div>
            </>
          ) : (
            <>
              {loading ? (
                <div className="text-center">
                  <Spinner animation="border" variant="primary" />
                  <p className="mt-3">Carregando QR Code...</p>
                </div>
              ) : (
                <>
                  <h5 className="mb-3 text-center">Pague com Pix</h5>
                  <div className="text-center mb-3">
                    <QRCode value={pixCode} size={200} />
                  </div>
                  <Form.Control
                    as="textarea"
                    rows={3}
                    readOnly
                    value={pixCode}
                    className="text-monospace mb-3"
                  />
                  <div className="text-center">
                    <Button variant="outline-primary" onClick={handleCopy}>
                      Copiar Código Pix
                    </Button>
                  </div>
                  {copied && (
                    <Alert variant="success" className="mt-3">
                      Código Pix copiado com sucesso!
                    </Alert>
                  )}
                  <div className="text-center mt-3">
                    <Button variant="secondary" onClick={goToDashboard}>
                      Ir para o Dashboard
                    </Button>
                  </div>
                </>
              )}
            </>
          )}
        </Col>
      </Row>
    </Container>
  );
}

export default Checkout;

// src/components/autenticacao/CriarConta.js
import React, { useState } from 'react';
import { Container, Form, Button, Row, Col, Image } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import Logo from "../../assets/imgs/idusbranca.png"

function CriarConta() {

  const MAIN_URL = process.env.REACT_APP_MAIN;

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  const { setIsLoggedIn } = useAuth(); // Usa setIsLoggedIn

  const handleCreateAccount = (e) => {
    e.preventDefault();

    // Simulação de criação de conta (substituir por chamada de API real)
    console.log('Conta criada para:', email);

    // Após criar a conta com sucesso, definir isLoggedIn como true
    setIsLoggedIn(true);
    navigate(MAIN_URL + 'dashboard');
  };

  return (
    <Container className="mt-5 d-flex justify-content-center align-items-center login-container" fluid>
      <Row className="w-100">
        <Col md={6} className="d-flex flex-column justify-content-center align-items-center text-center">
          <Link to={MAIN_URL} className="logo-link mb-4">
            <Image src={Logo} alt="Logo da Empresa" className="logo-img" />
          </Link>
          <h2 className="mb-3">Criar Conta</h2>
          <p className="text-muted">
            Crie sua conta para acessar o dashboard e gerenciar suas ferramentas de IA para social media.
          </p>

          <Form className="w-75 mt-4" onSubmit={handleCreateAccount}>
            <Form.Group controlId="formEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                placeholder="Digite seu email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </Form.Group>

            <Form.Group controlId="formPassword" className="mt-3">
              <Form.Label>Senha</Form.Label>
              <Form.Control
                type="password"
                placeholder="Digite sua senha"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </Form.Group>

            <Button variant="primary" type="submit" className="mt-4 w-100">
              Criar Conta
            </Button>

            <div className="mt-3">
              <Link to={MAIN_URL + 'login'} className="text-decoration-none">
                Já tem uma conta? Faça login
              </Link>
            </div>
          </Form>
        </Col>

        <Col md={6} className="d-none d-md-block bg-light p-0">
          <Image src="/path/to/side-image.jpg" alt="Imagem ilustrativa" fluid className="side-image" />
        </Col>
      </Row>
    </Container>
  );
}

export default CriarConta;

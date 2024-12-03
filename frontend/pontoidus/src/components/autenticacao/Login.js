// src/components/autenticacao/Login.js
import React, { useState } from "react";
import { Container, Form, Button, Row, Col, Image } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext"; // Importa useAuth
import Logo from "../../assets/imgs/idusbranca.png";
import Elemento from "../../assets/imgs/elemento-idus.png";
import "./login.css"
function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const { setIsLoggedIn } = useAuth(); // Usa setIsLoggedIn

  const MAIN_URL = process.env.REACT_APP_MAIN;

  const handleLogin = (e) => {
    e.preventDefault();
    setIsLoading(true);

    setTimeout(() => {
      setIsLoading(false);
      if (email === "usuario@teste.com" && password === "senha123") {
        setIsLoggedIn(true);
        navigate(MAIN_URL + "dashboard");
      } else {
        alert("Credenciais inválidas. Por favor, tente novamente.");
      }
    }, 1000);
  };

  return (
    <Container
      className="mt-5 d-flex justify-content-center align-items-center login-container"
      fluid
    >
      <Row className="w-100">
        <Col
          md={6}
          className="d-flex flex-column justify-content-center align-items-center text-center"
        >
          <Link to={MAIN_URL} className="logo-link mb-4">
            <Image src={Logo} alt="Logo da Empresa" className="logo-img" />
            <br />
            <br />
            <br />

          </Link>
          <h2 className="mb-3">Faça seu login</h2>
          <p className="text-muted">
            Entre com sua conta para acessar o dashboard e gerenciar sua jornada de trabalho.
          </p>

          <Form className="w-75 mt-4" onSubmit={handleLogin}>
            <Form.Group controlId="formEmail">
              <Form.Label>Matrícula</Form.Label>
              <Form.Control
                type="email"
                placeholder="Digite sua matricula"
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

            <Button
              variant="primary"
              type="submit"
              className="mt-4 w-100"
              disabled={isLoading}
            >
              {isLoading ? "Carregando..." : "Entrar"}
            </Button>

            <div className="mt-3">
              <Link
                to={MAIN_URL + "forgot-password"}
                className="text-decoration-none"
              >
                Esqueceu sua senha?
              </Link>
            </div>

            <div className="mt-3">
              <Link
                to={MAIN_URL + "criar-conta"}
                className="text-decoration-none"
              >
                Criar Conta
              </Link>
            </div>
          </Form>
        </Col>
        <Col md={6} className="d-none d-md-block transparent-bg p-0">
          <Image
            src={Elemento}
            alt="Imagem ilustrativa"
            fluid
            className="side-image"
          />
        </Col>
      </Row>
    </Container>
  );
}

export default Login;

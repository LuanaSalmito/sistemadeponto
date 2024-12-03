import React, { useState } from "react";
import {
  Container,
  Form,
  Button,
  Alert,
  Row,
  Col,
  Image,
} from "react-bootstrap";
import { Link } from "react-router-dom";
import Logo from "../../assets/imgs/idusbranca.png";
import Elemento from "../../assets/imgs/elementopc.png";
import "./forgotpassword.css";

function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handlePasswordReset = (e) => {
    e.preventDefault();
    // Simulação de recuperação de senha (substituir por chamada de API real)
    console.log("Instruções de recuperação enviadas para:", email);
    setSubmitted(true);
  };

  const MAIN_URL = process.env.REACT_APP_MAIN;

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
          </Link>
          <h2 className="mb-3">Esqueci a Senha</h2>
          <p className="text-muted">
            Insira seu email para receber instruções de recuperação de senha.
          </p>

          {submitted ? (
            <Alert variant="success" className="w-75">
              Instruções de recuperação de senha foram enviadas para seu email.
            </Alert>
          ) : (
            <Form className="w-75 mt-4" onSubmit={handlePasswordReset}>
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

              <Button variant="primary" type="submit" className="mt-4 w-100">
                Recuperar Senha
              </Button>
            </Form>
          )}

          <div className="mt-3">
            <Link to={MAIN_URL + "login"} className="text-decoration-none">
              Voltar para Login
            </Link>
          </div>
          <div className="mt-2">
            <Link to={MAIN_URL} className="text-decoration-none">
              Voltar para o Início
            </Link>
          </div>
        </Col>

        <Col
          md={6}
          style={{ backgroundColor: "transparent" }}
          className="d-none d-md-block p-0"
        >
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

export default ForgotPassword;

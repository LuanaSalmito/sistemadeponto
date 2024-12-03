import React from "react";
import {
  Container,
  Row,
  Col,
  Button,
  Card,
  Navbar,
  Nav,
  Accordion,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Inicio.css"
import Logo from "../../assets/imgs/logoidus.png"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCalendarAlt } from '@fortawesome/free-solid-svg-icons';

import { Link } from "react-router-dom";

function PaginaInicial() {
  const MAIN_URL = process.env.REACT_APP_MAIN;

  return (
    <>
   {/* Header */}
   <Navbar expand="lg" className="navbar-dark-blue shadow-sm mb-4 sticky-top">
      <Container className="container-header">
        <Navbar.Brand href="#inicio">
          <img className="logo" src={Logo} alt="" />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto">
            <Nav.Link href="#como-funciona">Como Funciona</Nav.Link>
            
            <Nav.Link href="#faq">Funcionalidades</Nav.Link>
            <Link className="btn btn-primary ms-2" to={MAIN_URL + "login"}>
              Login
            </Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>


      {/* Hero Section */}
      <section
        id="inicio"
        className="hero-section text-center"
        style={{
          backgroundImage: "url(/path/to/hero-background.jpg)",
          backgroundSize: "cover",
          padding: "150px 0",
        }}
      >
        <Container>
          <h1 className="display-4 animate__animated animate__fadeInDown">
            Gestão de Jornada Idus
          </h1>
          <p className="lead animate__animated animate__fadeInUp">
          Inovação Impulsionada pela Excelência.
          </p>
          <Link to={`${MAIN_URL}dashboard`}>
            <Button
              variant="dark"
              size="lg"
              className="shadow-sm animate__animated animate__pulse animate__infinite mx-4"
            >
              Bater ponto
            </Button>
          </Link>
          <a href="#planos">
            <Button
              variant="light"
              size="lg"
              className="shadow-sm animate__animated animate__pulse animate__infinite"
            >              Consultar matrícula

              
            </Button>
          </a>
        </Container>
      </section>

      {/* Vídeo de Demonstração */}
      <section id="demos" className="py-5">
        <Container>
          <h2 className="text-center mb-4">Tutorial de como entrar e bater o ponto diário</h2> <br />
          <br />
          <Row>
           
            <Col md={6}>
              <video controls width="100%" className="rounded shadow">
                <source src="path/to/demo-video.mp4" type="video/mp4" />
                Seu navegador não suporta a tag de vídeo.
              </video>
            </Col>
            <Col md={6}>
              <h3>Casos de Sucesso</h3>
              <p>
                Veja como nossa plataforma ajudou empresas como a sua a aumentar
                a presença online e engajamento.
              </p>
              <Button variant="primary">Leia Mais Casos</Button>
            </Col>
          </Row>
        </Container>
      </section>

      {/* Sobre Section */}
      <Container id="como-funciona" className="my-5">
        <Row className="align-items-center">
          

        </Row>
      </Container>

      {/* Funcionalidades */}
      <section id="funcionalidades" className="bg-light py-5">
        <br />
        <Container>
          <h2 className="text-center mb-4">Funcionalidades</h2>
          <Row className="g-4">
            {[
              {
                title: "Registro de Ponto Digital",
                text: "Possibilidade de registrar a presença remotamente via aplicativo.",
                icon: "calendar-alt",
              },
              {
                title: "Notificações e Alertas",
                text: " Lembretes automáticos para registro de ponto.",
                icon: "spell-check",
              },
              {
                title: "Relatórios de Jornada Personalizados",
                text: "Acesso fácil a históricos de registros, incluindo horas trabalhadas, extras e faltas.",
                icon: "lightbulb",
              },
            ].map((feature, index) => (
              <Col md={4} key={index}>
                <Card className="h-100 shadow-sm">
                  <Card.Body>
                    <div className="feature-icon mb-3">
                      <i
                        className={`fas fa-${feature.icon} fa-2x text-primary`}
                      ></i>
                    </div>
                    <Card.Title>{feature.title}</Card.Title>
                    <Card.Text>{feature.text}</Card.Text>
                  </Card.Body>
                </Card>
              </Col>
            ))}
          </Row>
          <br />
        </Container>
      </section>

  
      <footer className="bg-dark text-center text-white py-3">
        <Container>
          <p>&copy; 2024 Idus Inteligência Industrial. Todos os direitos reservados.</p>
          <Nav className="justify-content-center">
            <Nav.Link href="#inicio" className="text-white">
              Como funciona
            </Nav.Link>
            <Nav.Link href="#funcionalidades" className="text-white">
              Funcionalidades
            </Nav.Link>
            
          </Nav>
        </Container>
      </footer>
    </>
  );
}

export default PaginaInicial;

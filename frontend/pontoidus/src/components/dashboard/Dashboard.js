import React, { useState } from 'react';
import { Outlet, Link } from 'react-router-dom';
import Logout from '../autenticacao/Logout';
import { Container, Row, Col, Nav, Navbar, Image, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Dashboard.css';
import menuData from './menuData';
import Logo from "../../assets/imgs/idusbranca.png";

import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';
const MAIN_URL = process.env.REACT_APP_MAIN;
const dashboard = MAIN_URL + 'dashboard';
function Dashboard() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <Container fluid className="dashboard-container">
      {/* Navbar Superior */}
      <Navbar bg="light" expand="lg" className="fixed-top top-navbar shadow-sm">
        <Navbar.Brand as={Link} to={dashboard}>
          <Image className='logo-dashboard' src={Logo} height="40" alt="Logo da Empresa" />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbar-nav" />
        <Navbar.Collapse id="navbar-nav">
          <Nav className="ms-auto">
            
            <Logout />
          </Nav>
        </Navbar.Collapse>
      </Navbar>

      <Row className="dashboard-content" style={{ marginTop: '60px' }}>
        {/* Sidebar Menu */}
        <Col
          xs={12}
          md={isSidebarOpen ? 3 : 1}
          className={`sidebar bg-white p-4 border-end position-fixed h-100 overflow-auto shadow-sm pt-0 ${isSidebarOpen ? '' : 'collapsed'}`}
        >
          <span
            
            className="sidebar-toggle mb-2"
            onClick={toggleSidebar}
          >
            {isSidebarOpen ? <> <FaChevronLeft /> Encolher Menu </> : <FaChevronRight />}
          </span>
          <Nav className="flex-column mt-5">
            {menuData.map((section, sectionIdx) => (
              <React.Fragment key={sectionIdx}>
                <h6 className={`mt-4 mb-2 text-muted ${isSidebarOpen ? '' : 'd-none'}`}>{section.section}</h6>
                {section.items.map((item, itemIdx) => (
                  <Nav.Item key={itemIdx}>
                    <Nav.Link
                      as={Link}
                      to={`${dashboard}/${item.path}`}
                      className="text-dark sidebar-link d-flex align-items-center"
                    >
                      {React.createElement(item.icon, { className: 'me-3 sidebar-icon' })}
                      <span className={isSidebarOpen ? '' : 'd-none'}>{item.label}</span>
                    </Nav.Link>
                  </Nav.Item>
                ))}
              </React.Fragment>
            ))}
          </Nav>
        </Col>

        {/* Main Content Area */}
        <Col md={{ span: isSidebarOpen ? 9 : 11, offset: isSidebarOpen ? 3 : 1 }} className="main-content mt-4 container">
          <Outlet />
        </Col>
      </Row>
    </Container>
  );
}

export default Dashboard;

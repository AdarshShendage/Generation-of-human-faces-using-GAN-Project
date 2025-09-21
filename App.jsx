import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import About from "./components/About";
import Home from "./components/Home";
import Contact from "./components/Contact";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css"; // custom styles
import GANGenerator from "./components/GANGenerator";

import {
  Navbar,
  Nav,
  Container
} from "react-bootstrap";

function App() {
  return (
    <Router>
      {/* Navbar */}
      <Navbar expand="lg" className="modern-navbar sticky-navbar" sticky="top">
        <Container>
          <a href="/" style={{textDecoration:"None"}}><Navbar.Brand className="fw-bold text-white fs-3">
            FaceGen<span className="gradient-text">AI</span>
          </Navbar.Brand></a>
          <Navbar.Toggle aria-controls="basic-navbar-nav" className="bg-light" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto">
              <Nav.Link as={Link} to="/" className="nav-link-modern">
                Home
              </Nav.Link>
              <Nav.Link as={Link} to="/workspace" className="nav-link-modern">
                Work Space
              </Nav.Link>
              <Nav.Link as={Link} to="/about" className="nav-link-modern">
                About
              </Nav.Link>
              <Nav.Link as={Link} to="/contact" className="nav-link-modern">
                Contact
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      {/* Routes */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/workspace" element={<GANGenerator />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Router>
  );
}

export default App;

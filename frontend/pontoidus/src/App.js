import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './components/dashboard/Dashboard';
import Agendador from './components/funcionalidades/Agendador';
import AnalisePalavrasChave from './components/funcionalidades/AnalisePalavrasChave';
import EmpresasEPersonas from './components/configuracoes/EmpresasEPersonas';
import Configuracoes from './components/configuracoes/Configuracoes';
import AnaliseTom from './components/funcionalidades/AnaliseTom';

import Perfil from './components/perfil/Perfil';
import GerenciadorAssinatura from './components/assinatura/GerenciadorAssinatura';
import ModelosConteudo from './components/funcionalidades/ModelosConteudo';
import SugestoesHashtags from './components/funcionalidades/SugestoesHashtags';
import IntegracaoImagens from './components/funcionalidades/IntegracaoImagens';
import RecomendacoesSEO from './components/funcionalidades/RecomendacoesSEO';
import GeradorIdeiasConteudo from './components/funcionalidades/GeradorIdeiasConteudo';
import CorrecaoGramatical from './components/funcionalidades/CorrecaoGramatical';
import OtimizacaoConteudo from './components/funcionalidades/OtimizacaoConteudo';
import PredicoesEngajamento from './components/funcionalidades/PredicoesEngajamento';
import ReescritaPostagem from './components/funcionalidades/ReescritaPostagem';
import PaginaInicial from './components/inicio/Inicio';
import Login from './components/autenticacao/Login';
import CriarConta from './components/autenticacao/CriarConta';
import HistoricoEAprendizado from './components/configuracoes/HistoricoEAprendizado';
import Checkout from './components/checkout/Checkout';
import ForgotPassword from './components/autenticacao/ForgotPassword';
import { useAuth, AuthProvider } from './context/AuthContext'; 
import './App.css';


const MAIN_URL = process.env.REACT_APP_MAIN;

function ProtectedRoute({ children }) {
  const { isLoggedIn } = useAuth();
  if (!isLoggedIn) {
    return <Navigate to={MAIN_URL + 'login'} replace />;
  }
  return children;
}



function PublicRoute({ children }) {
  const { isLoggedIn } = useAuth();
  if (isLoggedIn) {
    return <Navigate to={MAIN_URL + 'dashboard'} replace />;
  }
  return children;
}

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path={MAIN_URL} element={<PaginaInicial />} />
          <Route
            path={`${MAIN_URL}login`}
            element={
              <PublicRoute>
                <Login />
              </PublicRoute>
            }
          />
          <Route
            path={`${MAIN_URL}criar-conta`}
            element={
              <PublicRoute>
                <CriarConta />
              </PublicRoute>
            }
          />
          <Route
            path={`${MAIN_URL}forgot-password`}
            element={
              <PublicRoute>
                <ForgotPassword />
              </PublicRoute>
            }
          />
          <Route path={`${MAIN_URL}checkout/:planId`} element={<Checkout />} />

          <Route
            path={`${MAIN_URL}dashboard/*`}
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          >
            {/* Dashboard routes remain the same as they are nested */}
            <Route path="agendador" element={<Agendador />} />
            <Route path="palavras-chave" element={<AnalisePalavrasChave />} />
            <Route path="historico-e-aprendizado" element={<HistoricoEAprendizado />} />
            <Route path="analise-tom" element={<AnaliseTom />} />
            <Route path="analise-palavras-chave" element={<AnalisePalavrasChave />} />
            <Route path="tom" element={<AnaliseTom />} />
            <Route path="perfil" element={<Perfil />} />
            <Route path="gerenciar-assinatura" element={<GerenciadorAssinatura />} />
            <Route path="modelos-conteudo" element={<ModelosConteudo />} />
            <Route path="sugestoes-hashtags" element={<SugestoesHashtags />} />
            <Route path="gerador-ideias" element={<GeradorIdeiasConteudo />} />
            <Route path="empresas-e-personas" element={<EmpresasEPersonas />} />
            <Route path="configuracoes" element={<Configuracoes />} />
            <Route path="reescrita-postagem" element={<ReescritaPostagem />} />
            <Route path="recomendacoes-seo" element={<RecomendacoesSEO />} />
            <Route path="otimizacao-conteudo" element={<OtimizacaoConteudo />} />
            <Route path="integracao-imagens" element={<IntegracaoImagens />} />
            <Route path="correcao-gramatical" element={<CorrecaoGramatical />} />
            <Route path="predicoes-engajamento" element={<PredicoesEngajamento />} />
            <Route
              index
              element={
                <h2>Bem-vindo ao Dashboard! Selecione uma funcionalidade no menu.</h2>
              }
            />
          </Route>
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;

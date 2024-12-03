// menuData.js
import {
    FaCalendarAlt,
    FaKey,
    FaAdjust,
    FaSpellCheck,
    FaLightbulb,
    FaImage,
    FaClipboardCheck,
    FaChartLine,
    FaSearch,
    FaRedo,
    FaHashtag,
    FaHistory,
    FaUserTie,
    FaToolbox,
    FaGlobe,
    FaProjectDiagram,
} from 'react-icons/fa';

const menuData = [
    {
        section: 'Jornada de trabalho',
        items: [
            {
                label: 'Bater ponto',
                icon: FaCalendarAlt,
                path: 'agendador',
            },
            {
                label: 'Espelho de ponto',
                icon: FaKey,
                path: 'analise-palavras-chave',
            },
            {
                label: 'Horas pendentes',
                icon: FaAdjust,
                path: 'analise-tom',
            },
            {
                label: 'Hora extra',
                icon: FaChartLine,
                path: 'predicoes-engajamento',
            },
        ],
    },
    {
        section: 'Suporte ao colaborador',
        items: [
            {
                label: 'Chamados finalizados',
                icon: FaClipboardCheck,
                path: 'otimizacao-conteudo',
            },
            {
                label: 'Informar compensação',
                icon: FaSearch,
                path: 'correcao-gramatical',
                
            },
            {
                label: 'Consultar chamado',
                icon: FaSpellCheck,
                path: 'recomendacoes-seo',
            },
            {
                label: 'Anexar atestado médico',
                icon: FaLightbulb,
                path: 'gerador-ideias',
            }
        ],
    },
    {
        section: 'Perfil',
        items: [
            {
                label: 'Meu perfil',
                icon: FaLightbulb,
                path: 'gerador-ideias',
            }
        ],
    },
    {
        section: 'Logout',
        items: [
            {
                label: 'Sair',
                icon: FaHistory,
                path: 'historico-e-aprendizado',
            }
        ],
    },
];

export default menuData;

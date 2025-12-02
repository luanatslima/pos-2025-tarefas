import {
  carregarMarcas,
  carregarModelos,
  carregarAnos,
  consultarFipe
} from './dom.js';

document.addEventListener('DOMContentLoaded', () => {
  carregarMarcas();
  document.getElementById('tipo').addEventListener('change', carregarMarcas);
  document.getElementById('marca').addEventListener('change', carregarModelos);
  document.getElementById('modelo').addEventListener('change', carregarAnos);
  document.querySelector('button').addEventListener('click', consultarFipe);
});

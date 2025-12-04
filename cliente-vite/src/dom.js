import {
  getMarcas,
  getModelos,
  getAnos,
  getVeiculo
} from './api.js'; 

function getTipoSelect() {
  return document.getElementById('tipo');
}
function getMarcaSelect() {
  return document.getElementById('marca');
}
function getModeloSelect() {
  return document.getElementById('modelo');
}
function getAnoSelect() {
  return document.getElementById('ano');
}
function getResultadoDiv() {
  return document.getElementById('resultado');
}

export async function carregarMarcas() {
  const tipo = getTipoSelect().value;
  const marcas = await getMarcas(tipo);
  const marcaSelect = getMarcaSelect();
  marcaSelect.innerHTML = '<option>Selecione</option>';
  marcas.forEach(marca => {
    marcaSelect.innerHTML += `<option value="${marca.codigo}">${marca.nome}</option>`;
  });

  getModeloSelect().innerHTML = '';
  getAnoSelect().innerHTML = '';
  getResultadoDiv().innerHTML = '';
}

export async function carregarModelos() {
  const tipo = getTipoSelect().value;
  const marca = getMarcaSelect().value;
  const data = await getModelos(tipo, marca);
  const modeloSelect = getModeloSelect();
  modeloSelect.innerHTML = '<option>Selecione</option>';
  data.modelos.forEach(modelo => {
    modeloSelect.innerHTML += `<option value="${modelo.codigo}">${modelo.nome}</option>`;
  });

  getAnoSelect().innerHTML = '';
  getResultadoDiv().innerHTML = '';
}

export async function carregarAnos() {
  const tipo = getTipoSelect().value;
  const marca = getMarcaSelect().value;
  const modelo = getModeloSelect().value;
  const anos = await getAnos(tipo, marca, modelo);
  const anoSelect = getAnoSelect();
  anoSelect.innerHTML = '<option>Selecione</option>';
  anos.forEach(ano => {
    anoSelect.innerHTML += `<option value="${ano.codigo}">${ano.nome}</option>`;
  });

  getResultadoDiv().innerHTML = '';
}

export async function consultarFipe() {
  const tipo = getTipoSelect().value;
  const marca = getMarcaSelect().value;
  const modelo = getModeloSelect().value;
  const ano = getAnoSelect().value;

  if (!tipo || !marca || !modelo || !ano) {
    alert("Por favor, selecione todos os campos.");
    return;
  }

  try {
    const dados = await getVeiculo(tipo, marca, modelo, ano);
    const resultadoDiv = getResultadoDiv();

    if (!dados || !dados.nome) {
      resultadoDiv.innerHTML = `<p style="color:white;">Nenhum dado encontrado para essa combinação.</p>`;
      return;
    }

    resultadoDiv.innerHTML = `
      <div class="card text-white bg-dark mt-3">
        <div class="card-body">
          <h5 class="card-title">${dados.nome}</h5>
          <p class="card-text"><strong>Valor:</strong> ${dados.valor}</p>
          <p class="card-text"><strong>Mês de referência:</strong> ${dados.mesReferencia}</p>
          <p class="card-text"><strong>Combustível:</strong> ${dados.combustivel}</p>
        </div>
      </div>
    `;
  } catch (error) {
    console.error("Erro na consulta:", error);
    getResultadoDiv().innerHTML = `<p style="color:white;">Erro ao consultar a API.</p>`;
  }
}

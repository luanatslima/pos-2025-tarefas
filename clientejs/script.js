const tipoSelect = document.getElementById('tipo');
  const marcaSelect = document.getElementById('marca');
  const modeloSelect = document.getElementById('modelo');
  const anoSelect = document.getElementById('ano');
  const resultadoDiv = document.getElementById('resultado');

  tipoSelect.addEventListener('change', carregarMarcas);
  marcaSelect.addEventListener('change', carregarModelos);
  modeloSelect.addEventListener('change', carregarAnos);

  async function carregarMarcas() {
    const tipo = tipoSelect.value;
    const res = await fetch(`https://parallelum.com.br/fipe/api/v1/${tipo}/marcas`);
    const marcas = await res.json();
    marcaSelect.innerHTML = '<option>Selecione</option>';
    marcas.forEach(marca => {
      marcaSelect.innerHTML += `<option value="${marca.codigo}">${marca.nome}</option>`;
    });
    modeloSelect.innerHTML = '';
    anoSelect.innerHTML = '';
    resultadoDiv.innerHTML = '';
  }

  async function carregarModelos() {
    const tipo = tipoSelect.value;
    const marca = marcaSelect.value;
    const res = await fetch(`https://parallelum.com.br/fipe/api/v1/${tipo}/marcas/${marca}/modelos`);
    const data = await res.json();
    modeloSelect.innerHTML = '<option>Selecione</option>';
    data.modelos.forEach(modelo => {
      modeloSelect.innerHTML += `<option value="${modelo.codigo}">${modelo.nome}</option>`;
    });
    anoSelect.innerHTML = '';
    resultadoDiv.innerHTML = '';
  }

  async function carregarAnos() {
    const tipo = tipoSelect.value;
    const marca = marcaSelect.value;
    const modelo = modeloSelect.value;
    const res = await fetch(`https://parallelum.com.br/fipe/api/v1/${tipo}/marcas/${marca}/modelos/${modelo}/anos`);
    const anos = await res.json();
    anoSelect.innerHTML = '<option>Selecione</option>';
    anos.forEach(ano => {
      anoSelect.innerHTML += `<option value="${ano.codigo}">${ano.nome}</option>`;
    });
    resultadoDiv.innerHTML = '';
  }

  async function consultarFipe() {
    const tipo = tipoSelect.value;
    const marca = marcaSelect.value;
    const modelo = modeloSelect.value;
    const ano = anoSelect.value;
    const res = await fetch(`https://parallelum.com.br/fipe/api/v1/${tipo}/marcas/${marca}/modelos/${modelo}/anos/${ano}`);
    const dados = await res.json();
    resultadoDiv.innerHTML = `
      <h2>Resultado:</h2>
      <p><strong>Veículo:</strong> ${dados.nome}</p>
      <p><strong>Valor:</strong> ${dados.valor}</p>
      <p><strong>Mês de referência:</strong> ${dados.mesReferencia}</p>
      <p><strong>Combustível:</strong> ${dados.combustivel}</p>
    `;
  }

  // Carrega marcas inicialmente
  carregarMarcas();



  const toggle = document.querySelector('#dark-mode-toggle');
  toggle.addEventListener('click', () => {
  if (document.body.classList.contains('dark-mode')) {
  document.body.classList.remove('dark-mode');
  toggle.innerHTML = "Desativar modo escuro";
  } else {
  document.body.classList.add('dark-mode');
  toggle.innerHTML = "Ativar modo escuro";
  }
  }); 
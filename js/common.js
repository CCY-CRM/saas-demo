// ===== 公共交互脚本 =====

// 导航高亮
(function() {
  var path = window.location.pathname;
  var filename = path.substring(path.lastIndexOf('/') + 1);
  var navItems = document.querySelectorAll('.sidebar-nav .nav-item');
  navItems.forEach(function(item) {
    var href = item.getAttribute('href');
    if (href && href === filename) {
      item.classList.add('active');
    }
  });
})();

// Tab 切换
function initTabs(container) {
  var tabs = container.querySelectorAll('.tab');
  var panels = container.querySelectorAll('.tab-panel');
  tabs.forEach(function(tab, idx) {
    tab.addEventListener('click', function() {
      tabs.forEach(function(t) { t.classList.remove('active'); });
      panels.forEach(function(p) { p.classList.add('hidden'); });
      tab.classList.add('active');
      if (panels[idx]) panels[idx].classList.remove('hidden');
    });
  });
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.tabs-container').forEach(initTabs);
});

// 模态框
function openModal(id) {
  var modal = document.getElementById(id);
  if (modal) modal.classList.remove('hidden');
}
function closeModal(id) {
  var modal = document.getElementById(id);
  if (modal) modal.classList.add('hidden');
}

// 侧边栏移动端切换
function toggleSidebar() {
  document.querySelector('.sidebar').classList.toggle('open');
}

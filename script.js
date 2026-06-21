document.getElementById('year').textContent = new Date().getFullYear();

const MONTHS_LONG = ['janvier','février','mars','avril','mai','juin',
    'juillet','août','septembre','octobre','novembre','décembre'];

function formatDateFr(dateStr) {
    if (!dateStr) return '';
    const [y, m, d] = dateStr.split('-');
    return `${parseInt(d)} ${MONTHS_LONG[parseInt(m) - 1]} ${y}`;
}

function parseFrontmatter(text) {
    const meta = {};
    if (!text.startsWith('---')) return { meta, body: text };
    const end = text.indexOf('---', 3);
    if (end === -1) return { meta, body: text };
    const fm = text.slice(3, end);
    const body = text.slice(end + 3).trim();
    fm.split('\n').forEach(line => {
        const m = line.match(/^(\w+):\s*"?([^"]*?)"?\s*$/);
        if (m) meta[m[1]] = m[2].trim();
    });
    return { meta, body };
}

async function loadMarkdown() {
    const params = new URLSearchParams(window.location.search);
    const file = params.get('file');
    const contentEl = document.getElementById('content');

    if (!file) {
        contentEl.innerHTML = '<p>Aucun fichier spécifié.</p>';
        return;
    }

    try {
        const resp = await fetch(file);
        if (!resp.ok) throw new Error('Fichier non trouvé');
        const text = await resp.text();
        const { meta, body } = parseFrontmatter(text);

        if (meta.titre) document.title = meta.titre + ' - BDE';

        const metaItems = [
            meta.date  ? `<span>${formatDateFr(meta.date)}</span>` : '',
            meta.heure ? `<span>${meta.heure}</span>` : '',
            meta.lieu  ? `<span>${meta.lieu}</span>`  : '',
        ].filter(Boolean).join('');

        const descHtml = body ? `
            <div class="event-section-label">Informations</div>
            <div class="event-description">${marked.parse(body)}</div>` : '';

        const posterHtml = meta.poster ? `
            <div class="event-poster">
                <img src="${meta.poster}" alt="Affiche — ${meta.titre}" />
            </div>` : '';

        contentEl.innerHTML = `
            <h1>${meta.titre || ''}</h1>
            ${metaItems ? `<div class="event-meta-detail">${metaItems}</div>` : ''}
            ${descHtml}
            ${posterHtml}
        `;
    } catch {
        contentEl.innerHTML = '<p>Erreur : impossible de charger cet événement.</p>';
    }
}

loadMarkdown();

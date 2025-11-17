// Sample cart data (sample courses)
const cart = [
  {
    id: "c1",
    title: "Data-driven Marketing (Practical)",
    instructor: "Lan Tran",
    option: "certificate",
    price: 79.0,
    qty: 1,
    thumb: "",
  },
  {
    id: "c2",
    title: "Frontend Basics: HTML & CSS",
    instructor: "Team Edu",
    option: "basic",
    price: 29.0,
    qty: 1,
    thumb: "",
  },
];

const TAX_RATE = 0.05;
let appliedCoupon = null;

// Utility: format currency
function fmt(v) {
  return "$" + v.toFixed(2);
}

// DOM refs
const summaryList = document.getElementById("summaryList");
const subtotalEl = document.getElementById("subtotal");
const discountEl = document.getElementById("discount");
const taxEl = document.getElementById("tax");
const totalEl = document.getElementById("total");

const r_subtotal = document.getElementById("r-subtotal");
const r_discount = document.getElementById("r-discount");
const r_tax = document.getElementById("r-tax");
const r_total = document.getElementById("r-total");

const miniSummary = document.getElementById("miniSummary");

const itemsList = document.getElementById("itemsList");

const couponInput = document.getElementById("coupon");
const applyCouponBtn = document.getElementById("applyCoupon");
const couponMessage = document.getElementById("couponMessage");

const step1 = document.getElementById("step-1");
const step2 = document.getElementById("step-2");
const step3 = document.getElementById("step-3");
const confirmation = document.getElementById("confirmation");

const stepInd1 = document.getElementById("step-ind-1");
const stepInd2 = document.getElementById("step-ind-2");
const stepInd3 = document.getElementById("step-ind-3");

// step navigation buttons
document.getElementById("toPayment").addEventListener("click", () => {
  // simple validation for required fields
  const name = document.getElementById("fullName").value.trim();
  const email = document.getElementById("email").value.trim();
  if (!name || !validateEmail(email)) {
    couponMessage.textContent =
      "Vui lòng nhập tên và email hợp lệ trước khi tiếp tục.";
    couponMessage.style.color = "red";
    return;
  }
  couponMessage.textContent = "";
  showStep(2);
});
document
  .getElementById("backToInfo")
  .addEventListener("click", () => showStep(1));
document.getElementById("toReview").addEventListener("click", () => {
  // basic card validation if card selected
  const payMethod = document.querySelector(
    'input[name="payMethod"]:checked'
  ).value;
  if (payMethod === "card") {
    const cn = document.getElementById("cardNumber").value.replace(/\s/g, "");
    if (!/^\d{16}$/.test(cn)) {
      document.getElementById("paymentError").textContent =
        "Card number không đúng định dạng.";
      return;
    }
  }
  document.getElementById("paymentError").textContent = "";
  renderItems();
  showStep(3);
});
document
  .getElementById("backToPayment")
  .addEventListener("click", () => showStep(2));
document.getElementById("placeOrder").addEventListener("click", placeOrder);
document
  .getElementById("backToCatalog")
  .addEventListener("click", () => alert("Navigate: back to catalog (demo)"));

// coupon apply
applyCouponBtn.addEventListener("click", () => {
  const code = couponInput.value.trim().toUpperCase();
  if (!code) {
    couponMessage.textContent = "Nhập mã giảm giá.";
    couponMessage.style.color = "red";
    return;
  }
  // demo: COUPON10 gives 10% off
  if (code === "COUPON10") {
    appliedCoupon = { code, percent: 10 };
    couponMessage.textContent = "Mã COUPON10 áp dụng: -10%";
    couponMessage.style.color = "green";
    recalcAll();
  } else {
    appliedCoupon = null;
    couponMessage.textContent = "Mã không hợp lệ hoặc đã hết hạn.";
    couponMessage.style.color = "red";
    recalcAll();
  }
});

// render top summary (used in step1 aside)
function renderSummary() {
  summaryList.innerHTML = "";
  cart.forEach((item) => {
    const li = document.createElement("li");
    li.innerHTML = `
      <img alt="" src="data:image/svg+xml;charset=UTF-8,${encodeURIComponent(
        makePlaceholderThumb(item.title)
      )}" />
      <div style="flex:1">
        <div style="font-weight:600">${escapeHtml(item.title)}</div>
        <div style="font-size:13px;color:#55606b">${escapeHtml(
          item.instructor
        )} • ${item.option}</div>
      </div>
      <div style="min-width:80px;text-align:right">${fmt(
        item.price * item.qty
      )}</div>
    `;
    summaryList.appendChild(li);
  });
  recalcAll();
}

// render mini summary for payment aside
function renderMiniSummary() {
  miniSummary.innerHTML = cart
    .map(
      (i) =>
        `<div>${escapeHtml(i.title)} <strong>${fmt(
          i.price * i.qty
        )}</strong></div>`
    )
    .join("");
}

// recalc totals
function recalcAll() {
  const sub = cart.reduce((s, i) => s + i.price * i.qty, 0);
  let discount = 0;
  if (appliedCoupon) discount = sub * (appliedCoupon.percent / 100);
  const tax = (sub - discount) * TAX_RATE;
  const total = Math.max(0, sub - discount + tax);

  subtotalEl.textContent = fmt(sub);
  discountEl.textContent = `-${fmt(discount)}`;
  taxEl.textContent = fmt(tax);
  totalEl.textContent = fmt(total);

  r_subtotal.textContent = fmt(sub);
  r_discount.textContent = `-${fmt(discount)}`;
  r_tax.textContent = fmt(tax);
  r_total.textContent = fmt(total);

  document.getElementById("confTotal").textContent = fmt(total);
}

// render items list in review with Edit & Remove
function renderItems() {
  itemsList.innerHTML = "";
  cart.forEach((item) => {
    const div = document.createElement("div");
    div.className = "cart-item";
    div.dataset.id = item.id;
    div.innerHTML = `
      <img alt="" src="data:image/svg+xml;charset=UTF-8,${encodeURIComponent(
        makePlaceholderThumb(item.title)
      )}" />
      <div class="meta">
        <div style="font-weight:700">${escapeHtml(item.title)}</div>
        <div style="font-size:13px;color:#55606b">${escapeHtml(
          item.instructor
        )} · ${item.option}</div>
        <div style="margin-top:8px;color:#55606b">Price: ${fmt(item.price)} × ${
      item.qty
    } = ${fmt(item.price * item.qty)}</div>
      </div>
      <div class="actions">
        <button class="small-btn btn-secondary edit-btn" data-id="${
          item.id
        }">Edit</button>
        <button class="small-btn btn-secondary remove-btn" data-id="${
          item.id
        }">Remove</button>
      </div>
    `;
    itemsList.appendChild(div);
  });

  // bind edit/remove
  document.querySelectorAll(".edit-btn").forEach((b) => {
    b.addEventListener("click", (e) => {
      const id = e.currentTarget.dataset.id;
      openEdit(id);
    });
  });
  document.querySelectorAll(".remove-btn").forEach((b) => {
    b.addEventListener("click", (e) => {
      const id = e.currentTarget.dataset.id;
      if (confirm("Bạn có chắc muốn xoá khóa học khỏi đơn?")) {
        removeItem(id);
      }
    });
  });

  // update review totals
  recalcAll();
}

// edit modal logic
const editModal = document.getElementById("editModal");
const editForm = document.getElementById("editForm");
const editCourseName = document.getElementById("editCourseName");
const editOption = document.getElementById("editOption");
const editQty = document.getElementById("editQty");
let editingId = null;

function openEdit(id) {
  editingId = id;
  const it = cart.find((x) => x.id === id);
  if (!it) return;
  editCourseName.textContent = it.title;
  editOption.value = it.option === "certificate" ? "certificate" : "basic";
  editQty.value = it.qty;
  editModal.classList.remove("hidden");
  // trap focus naive:
  document.getElementById("saveEdit").focus();
}
document.getElementById("cancelEdit").addEventListener("click", () => {
  editModal.classList.add("hidden");
});
document.getElementById("saveEdit").addEventListener("click", () => {
  const it = cart.find((x) => x.id === editingId);
  if (!it) return;
  it.option = editOption.value;
  it.qty = Math.max(1, Math.min(5, Number(editQty.value) || 1));
  // if option certificate, add $20 surcharge (adjust price for demo)
  if (it.id === "c1") {
    // demo: c1 base 59, certificate +20 => price 79
    it.price = it.option === "certificate" ? 79 : 59;
  } else {
    it.price =
      it.option === "certificate"
        ? it.id === "c2"
          ? 49
          : 29
        : it.id === "c2"
        ? 29
        : 29;
  }
  editModal.classList.add("hidden");
  renderSummary();
  renderItems();
});

// remove item
function removeItem(id) {
  const idx = cart.findIndex((x) => x.id === id);
  if (idx >= 0) {
    cart.splice(idx, 1);
    renderSummary();
    renderItems();
  }
}

// place order (simulate create)
function placeOrder() {
  const agreed = document.getElementById("agreeTerms").checked;
  if (!agreed) {
    alert("Vui lòng đồng ý điều khoản trước khi đặt hàng.");
    return;
  }
  // simulate order creation
  const orderId =
    "ORD-" +
    new Date().toISOString().slice(0, 10).replace(/-/g, "") +
    "-" +
    Math.floor(Math.random() * 900 + 100);
  document.getElementById("orderId").textContent = orderId;

  // populate confirmation details
  const cList = document.getElementById("confItems");
  cList.innerHTML = "";
  cart.forEach((i) => {
    const li = document.createElement("li");
    li.textContent = `${i.title} — ${i.option} — ${i.qty} × ${fmt(
      i.price
    )} = ${fmt(i.qty * i.price)}`;
    cList.appendChild(li);
  });

  // hide step forms, show confirmation
  step1.classList.add("hidden");
  step2.classList.add("hidden");
  step3.classList.add("hidden");
  confirmation.classList.remove("hidden");
  // clear cart (demo)
  // cart.length = 0;
}

// helper show step
function showStep(n) {
  step1.classList.add("hidden");
  step2.classList.add("hidden");
  step3.classList.add("hidden");
  stepInd1.removeAttribute("aria-current");
  stepInd2.removeAttribute("aria-current");
  stepInd3.removeAttribute("aria-current");

  if (n === 1) {
    step1.classList.remove("hidden");
    stepInd1.setAttribute("aria-current", "step");
  }
  if (n === 2) {
    step2.classList.remove("hidden");
    stepInd2.setAttribute("aria-current", "step");
    renderMiniSummary();
  }
  if (n === 3) {
    step3.classList.remove("hidden");
    stepInd3.setAttribute("aria-current", "step");
    renderItems();
  }

  window.scrollTo({ top: 0, behavior: "smooth" });
}

// helpers
function validateEmail(e) {
  return /\S+@\S+\.\S+/.test(e);
}
function escapeHtml(s) {
  return String(s).replace(
    /[&<>"']/g,
    (ch) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[
        ch
      ])
  );
}

// placeholder thumb generator (inline SVG)
function makePlaceholderThumb(title) {
  const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='160' height='100'>
    <rect width='100%' height='100%' fill='#f3f6f9' rx='8'/>
    <text x='10' y='55' font-size='12' fill='#55606b' font-family='Arial'>${title.slice(
      0,
      28
    )}</text>
  </svg>`;
  return svg;
}

// initial render
renderSummary();
renderMiniSummary();
recalcAll();
showStep(1);

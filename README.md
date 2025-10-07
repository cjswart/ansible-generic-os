# 🧱 Ansible Infrastructure Automation

A production-ready, CI/CD-integrated Ansible framework.

---

## 🚀 Features
- ✅ Environment-based inventories (dev, stage, prod)
- ✅ CI/CD with GitHub Actions
- ✅ Automated linting & Molecule testing
- ✅ Secure secrets via Ansible Vault
- ✅ Reusable roles with test coverage

---

## 🧩 Quick Start

```bash
# 1️⃣ Install dependencies
pip install ansible ansible-lint molecule[docker] testinfra docker

# 2️⃣ Run Molecule tests
cd roles/common
molecule test

# 3️⃣ Lint playbooks
ansible-lint playbooks/

# 4️⃣ Deploy manually (example)
ansible-playbook playbooks/site.yml -i inventories/dev/hosts.yaml

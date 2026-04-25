provider "google" {

  project = var.projectID
  region  = var.region
  zone    = var.location

}

resource "google_compute_network" "TestVPC" {
  name                    = "testvpc"
  auto_create_subnetworks = false

}

resource "google_compute_subnetwork" "public_network" {
  name          = "testsubnet"
  ip_cidr_range = "192.168.0.0/24"
  region        = var.region
  network       = google_compute_network.TestVPC.id


}
resource "google_compute_instance" "testVM" {
  name           = "testvm"
  machine_type   = var.machine_type
  zone           = var.location
  desired_status = "TERMINATED"
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      labels = {
        my_label = "TestVM"
      }
    }
  }
  network_interface {
    network    = google_compute_network.TestVPC.id
    subnetwork = google_compute_subnetwork.public_network.id
    network_ip = "192.168.0.10"

    access_config {
      // Ephemeral public IP

    }
  }
}
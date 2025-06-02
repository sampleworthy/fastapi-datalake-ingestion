provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "datalake" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true

  tags = {
    environment = var.environment
  }
}

resource "azurerm_storage_data_lake_gen2_filesystem" "fs" {
  name               = var.file_system_name
  storage_account_id = azurerm_storage_account.datalake.id
}

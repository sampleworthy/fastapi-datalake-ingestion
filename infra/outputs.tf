output "storage_account_name" {
  value = azurerm_storage_account.datalake.name
}

output "file_system_name" {
  value = azurerm_storage_data_lake_gen2_filesystem.fs.name
}
output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}
output "location" {
  value = azurerm_resource_group.rg.location
}
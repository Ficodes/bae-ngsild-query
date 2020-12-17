# BAE NGSI-LD Query Extension

BAE extension for the monetization of NGSI-LD Queries using a FIWARE Keyrock
as IDM.

This extension requires an application ID and a role name to be provided, during
product creation the extension will check for the role (+ .admin) in the Keyrock
Application, and will create it if not present.

Once the product is acquired, the customer will be granted the new role in the
Keyrock application.

## Configuration

To work properly, this extension requires the foolowing evironment variables
to have been configured in the BAE Charging Backend component

* **BAE_ASSET_IDM_USER**: Admin user used to access Keyrock APIs
* **BAE_ASSET_IDM_PASSWORD**: Password of admin user used to access Keyrock APIs
* **BAE_ASSET_IDM_URL**: URL of the Keyrock instance

package filepanel

import "github.com/Noswad123/wyrm/src/internal/common"

func (p PanelMode) String() string {
	switch p {
	case SelectMode:
		return "selectMode"
	case BrowserMode:
		return "browserMode"
	default:
		return common.InvalidTypeString
	}
}
